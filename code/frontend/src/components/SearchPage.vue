<script setup>
import { ref, onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import UserTopbar from './topBar/UserTopbar.vue';
import router from '@/router';


const route = useRoute();
const keyword = ref(route.params.keyword);
const token = ref(sessionStorage.getItem('MusicalToken'));
const empty = ref(false);
const songs = ref([])
const albums = ref([])
const creators = ref([])

addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        router.go();
    }
});

onBeforeMount(async () => {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/search?keyword=${keyword.value}`);
    const data = await response.json();
    console.log(data);
    if (!(data.songs.length | data.albums.length | data.creators.length )) {
        empty.value = true;
        return
    }
    songs.value = data.songs;
    albums.value = data.albums;
    creators.value = data.creators;


});

</script>
<template>
    <UserTopbar  :logged="token"/>
    <div class="text-white pt-2">
        <h2 class="p-2"><span class="text-white-50 ">RESULTS FOR :</span> {{keyword}}</h2>
        <div>
            <p v-show="empty" class="fs-2 p-2">NO RESULTS FOUND</p>
                <div class="row ms-4 me-4 ">
                    <h3 v-show="creators.length">Creators</h3>
                    <div class="p-2 col bg-custom mx-2 my-1 " v-for="(i,index) in creators" :key=index >

                        <router-link :to="`/creator/${i.creator_id}`"><img :src="`/creator/${ i.creator_id }.jpg`" style="width: 13rem;" :alt="`${i.creator_name}`"></router-link>
                        <p class="text-white text-center m-1 mb-0">{{ i.creator_name }}</p>
                    </div>

                    <h3 v-show="albums.length">Albums</h3>
                    <div v-show="albums" class="p-2 col bg-custom mx-2 my-1 " v-for="(i,index) in albums" :key=index>
                        <router-link :to="`/album/${i.album_id}`"><img :src="`/album/${ i.album_id }.jpg`" style="width: 13rem;" alt="{{ i.album_name }}"></router-link>
                        <p class="text-white text-center m-1 mb-0">{{ i.album_name }}</p>
                    </div>

                    <h3 v-show="songs">Songs</h3>
                    <div v-show="songs" class="p-2 col bg-custom mx-2 my-1 " v-for="(i,index) in songs" :key=index>

                        <router-link :to="`/song/${i.song_id}`"><img :src="`/song/${ i.song_id }.jpg`" style="width: 13rem;" alt="{{ name }}"></router-link>
                        <p class="text-white text-center m-1 mb-0">{{ i.song_name }}</p>
                    </div>
                </div>
            </div>
    </div>
<!-- </div> -->
</template>

<style scoped>
.bg-custom{
    background-color: rgba(255, 255, 255, 0.158);
}
.bg-custom:hover{
    background-color: rgba(255, 255, 255, 0.058);
}
a{
    text-decoration: none;
}
.col{
    flex:0 1 15%;
}

</style>