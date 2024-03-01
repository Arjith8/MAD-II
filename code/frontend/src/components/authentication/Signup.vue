<script setup>

import { ref } from 'vue';

</script>

<template>
<div class="position-absolute top-50 start-50 translate-middle ">

    <div class="p-4 rounded rounded-5 bg-white text-center custom-width">
        <img src="../../assets/normal.png" style="width: 150px;">
        <h1 class="p-2">SIGN UP</h1>

        
        <label for="f_name" class="form-label p-2">FIRST NAME : </label>
        <input type="text" name="f_name" class="form-control border-dark-subtle ">


        <label for="l_name" class=" form-label p-2 ">LAST NAME : </label>
        <input name="l_name" type="text" class="form-control border-dark-subtle">  
        

        <label for="user" aria-disabled="true" class="form-label p-2">USERNAME : </label>
        <input type="text" name="user" class="form-control border-dark-subtle" required /> 

        <label for="pass" class="fs-6 form-label p-2">PASSWORD : </label>
        <input type="password" name="pass" class="form-control border-dark-subtle"  required /> <br>

        <button class="border border-primary btn btn-primary">SIGN UP</button>
            
    </div>

</div>

</template>


<style scoped>
.custom-width{
    width: 26rem;
    height: 37rem;
}
.custom-pb{
    padding-bottom: .5rem;
}


</style>
<!DOCTYPE html>
