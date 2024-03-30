<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import UserTopbar from '@/components/topBar/UserTopbar.vue';
const token = ref(sessionStorage.getItem('MusicalToken'))
const album_name = ref('')
const thumbnail = ref(null)
const router = useRouter()
const genre = ref('')
const songs = ref([]);
const song1 = ref('')
const song2 = ref('')
const song3 = ref('')
const song4 = ref('')
const song5 = ref('')
const song6 = ref('')


const onFileChange = (e) => {
    thumbnail.value = e.target.files[0]
}


console.log(songs.value)
async function createAlbum(){
    const formData = new FormData()
    songs.value = []
    if (!album_name.value || !thumbnail.value || !song1.value){
        alert("Please fill atleast the first song and the Albim name and thumbnail")
        return
    }
    formData.append('album_name', album_name.value)
    formData.append('thumbnail', thumbnail.value)
    songs.value.push(song1.value)
    songs.value.push(song2.value)
    songs.value.push(song3.value)
    songs.value.push(song4.value)
    songs.value.push(song5.value)
    songs.value.push(song6.value)

    formData.append('songs', songs.value)
    formData.append('genre', genre.value)
    for (let [key, value] of formData.entries()) {
        console.log(key, value);
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/album`,{
        method:"POST",

        headers:{
            "Authorization":`${token.value}`,
            // "Content-Type":"multipart/form-data"
        },
        body:formData
    })
    if (response.status == 401){
        alert("Please Login to create a album, redirecting in 5 seconds")
        setTimeout(() => {
            router.push('/login')
        }, 5000);
        return
    }
    const data = await response.json()

    if (!data.success){
        alert(data.message)
        return
    }

    alert("album Created")
    router.push('/creator_menu')

}

</script>

<template>
    <UserTopbar :logged="token" />
    <div class="row justify-content-center " style="height: 92vh" >
        <div class="col-auto bg-white p-3 rounded-4 " style="width: 50vw;">
            <div>
                <div class="p-2">
                    <div class="form-floating mb-3 ">
                        <input type="text" class="form-control " name="name" required v-model="album_name"> 
                        <label for="name" class="">album Name :</label>
                    </div>
                        <label for="picture" class="form-label ">Thumbnail</label>
                        <input type="file" name="thumbnail" class="form-control " accept=".jpg" @change="onFileChange" required>

                        <label for="genre" class="form-label ">Genre :</label>

                        <label for="genre" class="ps-4 pe-1">Pop </label>
                        <input type="radio" class="form-switch" name="genre" value="Pop" required v-model="genre">

                        <label for="genre" class="ps-4 pe-1  ">Jazz </label>
                        <input type="radio" class="form-switch " name="genre" value="Jazz" v-model="genre">

                        <label for="genre" class="ps-4 pe-1  ">Electronic </label>
                        <input type="radio" class="form-switch " name="genre" value="Electronic" v-model="genre">

                        <label for="genre" class="ps-4 pe-1  ">Instrumental </label>
                        <input type="radio" class="form-switch " name="genre" value="Instrumental" v-model="genre"> <br>
                        <label for="exampleDataList" class="form-label pt-2">Music 1 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." required v-model="song1" >
                        <label for="exampleDataList" class="form-label pt-2">Music 2 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song2">
                        <label for="exampleDataList" class="form-label pt-2">Music 3 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song3">
                        <label for="exampleDataList" class="form-label pt-2">Music 4 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song4">
                        <label for="exampleDataList" class="form-label pt-2">Music 5 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song5">
                        <label for="exampleDataList" class="form-label pt-2">Music 6 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song6">
                    <div class="pt-4">
                        <button type="submit" class="btn btn-primary " @click="createAlbum">SUBMIT</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>