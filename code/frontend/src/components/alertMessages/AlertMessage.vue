<script setup>
// import { defineProps } from 'vue';

const props = defineProps({
    message : String
})
</script>


<template>
    <p class="p-2 w-auto bg-danger ">{{ message }} </p>
</template>