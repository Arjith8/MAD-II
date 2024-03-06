<script setup>

</script>

<template>
    <div class="bg-custom">
        <slot></slot>
    </div>
</template>

<style scoped>
.bg-custom{
    background-color: rgba(255, 255, 255, 0.158);
}
.bg-custom:hover{
    background-color: rgba(255, 255, 255, 0.058);
}

</style>