<script setup>
import { ref, onBeforeMount } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import UserTopbar from '@/components/topBar/UserTopbar.vue';
import AlertMessage from '@/components/alertMessages/AlertMessage.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const router = useRouter()
const route = useRoute()

const data = ref({})
const song_name = ref('')
const lyrics = ref('')
const genre = ref('')
const message = ref('')
const alert = ref(false)

async function makeChanges(){
    if (!song_name.value || !lyrics.value || !genre.value){
        message.value = 'Please fill all the fields'
        alert.value = true
        setTimeout(()=>{
            alert.value = false
        }, 5000)
        return
    }

    const response = await fetch(`http://127.0.0.1:5000/api/v1/song_operation`, {
        method: 'PUT',
        headers: {
            "Authorization": `${token.value}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "song_id": route.params.id, 
            "song_name": song_name.value,
            "lyrics": lyrics.value,
            "genre": genre.value
        })
    })

    const data = await response.json()

    if (data.success){
        confirm('Changes made successfully')
        router.push('/creator_menu')
    } else {
        message.value = data.message
        alert.value = true
        setTimeout(()=>{
            alert.value = false
        }, 5000)
    }
}


onBeforeMount(async ()=>{
    if (!token.value){
        router.push('/login')
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/song?song_id=${route.params.id}`, {
        headers: {
            "Authorization": `${token.value}`
        }
    })

    data.value = await response.json()
    song_name.value = data.value.name
    genre.value = data.value.genre
    lyrics.value = data.value.lyrics
})

</script>



<template>
    <UserTopbar :logged="token"/>
    <AlertMessage v-show="alert" :message="message"/>
    <div class="row justify-content-center ">
        <div class=" col-auto bg-white rounded-4 text-black p-4" style="width:40vw">
            <h1>Edit Menu</h1>
            <div >
                <label for="Name" class="form-label ">Song Name : </label>
                <input type="text"  class="form-control " v-model="song_name">
                <div class=" pt-2">

                    <label for="genre" class="form-label ">Genre :</label>
        
                    <label for="genre" class="ps-4 pe-1">Pop </label>
                    <input type="radio" class="form-switch" name="genre" value="Pop" v-model="genre">
        
                    <label for="genre" class="ps-4 pe-1  ">Jazz </label>
                    <input type="radio" class="form-switch " name="genre" value="Jazz" v-model="genre">
        
                    <label for="genre" class="ps-4 pe-1  ">Electronic </label>
                    <input type="radio" class="form-switch " name="genre" value="Electronic" v-model="genre">
        
                    <label for="genre" class="ps-4 pe-1  ">Instrumental </label>
                    <input type="radio" class="form-switch " name="genre" value="Instrumental" v-model="genre">
                </div>
                <label for="lyrics" class="form-label ">Lyrics : </label>
                <textarea name="lyrics" type="text" class="form-control" rows="15" >{{data.lyrics}}</textarea>
                
                <button class="btn btn-primary p-1 px-2" @click="makeChanges">Submit</button>
            </div>
        </div>
    </div>
</template>