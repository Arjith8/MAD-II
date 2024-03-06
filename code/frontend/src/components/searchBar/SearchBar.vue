<script setup>

import { ref } from 'vue';
const inputValue = ref('')
const token = sessionStorage.getItem('MusicalToken')
function dataFetch(){
    const url = new URL('http://127.0.0.1:5000/search');
    url.searchParams.append('inputValue', inputValue.value);
    fetch(url,{
        method:'GET',
        headers:{
            'Content-Type':'application/json',
            'Authorization':token
        },
    })
}
</script>

<template>
    <input type="text" @keydown.enter="dataFetch" v-model="inputValue" style="width: 20rem; border: #0db1a4; height: 2.2rem;" class="p-1 px-2 rounded-3 " placeholder="SEARCH" name="search">
</template>