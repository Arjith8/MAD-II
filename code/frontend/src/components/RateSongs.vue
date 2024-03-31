<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';


const router = useRouter()
const rating = ref(0)
const props = defineProps(['song_id','token'])
async function submitRating(){

    console.log(rating.value)
    const response = await fetch("http://127.0.0.1:5000/api/v1/rate",{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'authorization': props.token
        },
        body: JSON.stringify({
            rating: rating.value,
            song_id: props.song_id
        })
    })
    const data = await response.json()
    if (data.success){
        alert("Rating Submitted")
        router.go()
    }else if (response.status == 401){
        alert("Please Login to Rate songs, redirecting in 5 seconds")
        setTimeout(() => {
            router.push('/login')
        }, 5000);
    }
    else{
        alert("Rating not submitted")
    }

}
</script>

<template>
    <div class="text-white form-check-inline ">
        <input type="radio" name="rating" value="1" class="form-check-input" v-model="rating" required><label for="1" class="form-check-label px-1"> 1</label>
        <input type="radio" name="rating" value="2" class="form-check-input" v-model="rating"><label for="2" class="form-check-label px-1"> 2</label>
        <input type="radio" name="rating" value="3" class="form-check-input" v-model="rating"><label for="3" class="form-check-label px-1"> 3</label>
        <input type="radio" name="rating" value="4" class="form-check-input" v-model="rating"><label for="4" class="form-check-label px-1"> 4</label>
        <input type="radio" name="rating" value="5" class="form-check-input" v-model="rating"><label for="5" class="form-check-label px-1"> 5</label>
        <button type="submit" class="btn btn-success " style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;" @click="submitRating">Submit Rating</button>
    </div><br>
</template>