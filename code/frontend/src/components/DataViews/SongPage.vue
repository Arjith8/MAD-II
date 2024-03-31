<script setup>
import { ref, onBeforeMount, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
// import AlertMessage from '../alertMessages/AlertMessage.vue';
import RateSongs from '../RateSongs.vue';
import UserTopbar from '../topBar/UserTopbar.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const logged = ref(false)
const router = useRouter()
const route = useRoute()
const song_data = ref({})
const song_id = ref()



onBeforeMount(async()=>{
    song_id.value = route.params.id
    try{
        console.log(song_id.value)
        const response = await fetch(`http://127.0.0.1:5000/api/v1/song?song_id=${song_id.value}`,{
            headers:{
                "Content-Type":"application/json",
            }
        })
        song_data.value = await response.json()
    }catch(e){
        console.log(e)
    }
    
})

async function addToFav(){
    const response = await fetch(`http://127.0.0.1:5000/api/v1/favourites?song_id=${song_id.value}`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "Authorization":`${token.value}`
        }
    })
    if (response.status == 401){
        alert("Please Login to add to Favourite, redirecting in 5 seconds")
        setTimeout(() => {
            router.push('/login')
        }, 5000);
        return
    }
    const data = await response.json()
    if (!data.success){
        alert(data.msg)
        return
    }
    alert("Added to Favourite")
    router.go()

}

async function flagged(){
    const response = await fetch(`http://127.0.0.1:5000/api/v1/flag?song_id=${song_id.value}`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "Authorization":`${token.value}`
        }
        
    })
    if (response.status == 401){
        alert("Please Login to Flag songs, redirecting in 5 seconds")
        setTimeout(() => {
            router.push('/login')
        }, 5000);
        return
    }
    const data = await response.json()
    console.log(data)
    if (!data.success){
        alert(data.msg)
        return
    }
    alert("Flagged Successfully")
    
}
</script>

<template>
    <UserTopbar :logged="token"/>
    <div class="row justify-content-center " style="height: 92.2vh; opacity: 95%;">
        <div class="col-auto px-4 rounded-2" style="background-color: #525452;">
            <div class="text-center " >
                <h1 class="text-white pt-1">{{song_data.name}} </h1>
                <h3 class="text-white fs-6 "><a class="text-white" href="/see/artist/{{song_data.singer_name}}">{{song_data.singer_name}} </a> | {{song_data.release_date}}</h3>
                <RateSongs :song_id="song_id" :token="token"/>
                <p class="text-white pt-2">
                    Rating : {{ song_data.rating }} 
                    <button class="btn btn-primary" @click="addToFav">Add to Favourite</button>
                    <button class="btn btn-danger" @click="flagged">Flag</button>
                </p>
                                
                <iframe class="bg-black" style="width:31rem;height:26.5rem ; opacity: 70%;" :src="`/lyrics/${song_id}.txt`" frameborder="" scrolling="auto"></iframe>
            </div> 
            <div class="text-center">
                <audio :src="`/tracks/${song_id }.mp3`" controls></audio>

            </div>
        </div>
    </div>
</template>

<style scoped>
    .custom-bg{
        background-color: #10c2b3;
    }
    body {
        background-image: url('../../../static/Image/{{data.song_name}}.jpg'); 
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .creator:hover{
        color:rgb(247, 247, 9)
    }
    .account:hover{
        color: rgb(5, 55, 125);
    }
    .logout:hover{
        color:rgb(255, 0, 76)
    }
    a{
        text-decoration: none;
    }
</style>