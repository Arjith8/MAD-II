<script setup>
import { ref, onBeforeMount } from 'vue'
import AlertMessage from './alertMessages/AlertMessage.vue';
import UserTopbar from './topBar/UserTopbar.vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter()
const route = useRoute()
const alert_ = ref(false)
const name = ref('')
const lyrics = ref('')
const lyrics_id = ref(route.params.id)
const token = ref(sessionStorage.getItem('MusicalToken'))
const message = ref('')

onBeforeMount(async ()=>{
    if (!token.value){
        router.push('/')
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/lyrics?lyrics_id=${lyrics_id.value}`,{
        headers:{
            'Content-Type':'application/json'
        }
    })
    const data = await response.json()
    console.log(data)
    name.value = data.lyrics_name
    lyrics.value = data.lyrics

})

async function sendLyrics(){
    const response = await fetch(`http://127.0.0.1:5000/api/v1/lyrics?lyrics_id=${lyrics_id.value}`,{
        method:'PUT',
        headers:{
            'Content-Type':'application/json',
            'Authorization': token.value
        },
        body:JSON.stringify({
            'lyrics_id':lyrics_id.value,
            'lyrics_name':name.value,
            'lyrics':lyrics.value
        })
    })
    const data = await response.json()
    console.log(data)
    if (data.success){
        alert('Lyrics updated successfully')
        router.push('/creator_menu')
    }
    else{
        alert_.value = true
        message.value = data.msg
    }
}
</script>

<template>
    <UserTopbar :logged="token"/>
    <div class=" row justify-content-center ">
        <div class="col-auto bg-white p-4 rounded-3 " style="width:50vw">
            <div>
                <h1 class="text-center ">Create Lyrics</h1>
                <label for="lyrics_name" class="form-label ">Lyrics Name : </label>
                <input type="text" name="lyrics_name" class="form-control border border-dark" v-model="name">
                <label for="lyrics" class="form-label ">Lyrics :</label>
                <div v-if="!alert_">
                    <textarea  name="lyrics" type="text" class="form-control  border-dark" rows="16" v-model="lyrics"></textarea><br>
                </div>
                <div v-else>
                    <textarea name="lyrics" type="text" class="form-control  border-dark" rows="15" v-model="lyrics"></textarea><br>
                    <AlertMessage  :message=message />
                </div>

                <button @click="sendLyrics" class="btn btn-primary">Submit</button>
            </div>
        </div>
    </div>
</template>