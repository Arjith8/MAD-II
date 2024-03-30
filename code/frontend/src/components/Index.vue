<script setup>
import { onBeforeMount, onMounted, ref } from 'vue';
import UserTopbar from '@/components/topBar/UserTopbar.vue';
import { useIndexStore } from '@/store/indexStore';
import ContentRowsIndex from './Rows/ContentRowsIndex.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const songs = ref('')
const creators = ref('')
const albums = ref('')
const favourites = ref([])
const logged = ref(false)
const indexStore = useIndexStore()

onBeforeMount(async ()=>{
    if (token.value){
        // console.log(toke)
        await indexStore.getFavourites(token.value)
        favourites.value = indexStore.favourites
        logged.value = true
        console.log(favourites.value)
    }
    await indexStore.getSongs()
    await indexStore.getCreators()
    songs.value = indexStore.songs;
    console.log(songs.value)
    creators.value = indexStore.creators
    console.log(creators.value)
    await indexStore.getAlbums()

    albums.value = indexStore.albums

})
</script>

<template>
    <UserTopbar :logged="logged" />
    <ContentRowsIndex v-show="favourites.length" :data="favourites" route="/song" title="FAVOURITES"/>
    <ContentRowsIndex :data="songs" route="/song" title="TOP SONGS"/>
    <ContentRowsIndex :data="creators" route="/creator" title="TOP CREATORS"/>
    <ContentRowsIndex :data="albums" route="/album" title="TOP ALBUMS"/>


			<!-- {% set len = favourites |length %}

			{% for name in favourites %}
			
			{%endfor%}

			
			{% if len < 5 %}
			{%set num=5-len%}
			<div class="p-2 col bg-custom mx-3 for_fun align-middle ">
				<p class="d-flex justify-content-center ">{{num}}</p>
			</div> 
			{%endif%}
			
		</div> -->

    <!-- </div> -->
</template>