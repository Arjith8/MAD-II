<script setup>
import { defineProps } from 'vue';
import { RouterView } from 'vue-router';
const props = defineProps({
    data : Object,
    title : String,
    route : String
})



</script>

<template>
    <div>
        <h1 class="text-white pt-2">{{title}}</h1>
        <div class="d-grid text-end">
            <router-link :to="`/seemore${route}`" class="d-grid pe-1">SEE MORE</router-link>
        </div>
		<div class="row">
            <div v-for="i in data" class="p-2 bg-custom mx-3" style="width: 17.33%; ">
                <router-link :to="`${route}/${i.id}`">
                    <img :src="`${route}/${i.id}.jpg`" style="width: 13rem;" :alt="i.id" >
                </router-link>
                <p class="text-white text-center m-1 mb-0 ">{{i.name}}</p>
            </div>
        </div>
    </div>
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
</style>
