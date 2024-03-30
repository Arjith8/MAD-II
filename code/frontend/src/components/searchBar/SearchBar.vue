<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const inputValue = ref('')
const token = sessionStorage.getItem('MusicalToken')
const router = useRouter()
function dataFetch(){
    if (inputValue.value){
        router.push(`/search/${inputValue.value}`)
    }
}

</script>

<template>
    <input type="text" @keydown.enter="dataFetch" v-model="inputValue" style="width: 20rem; border: #0db1a4; height: 2.2rem;" class="p-1 px-2 rounded-3 " placeholder="SEARCH" name="search">
</template>