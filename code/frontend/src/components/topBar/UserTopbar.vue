<script setup>
import TopBarWrapper from '@/components/wrappers/TopBarWrapper.vue';
import LogoIcon from "@/components/icons/IconLogo.vue";
import SearchBar from '@/components/searchBar/SearchBar.vue';
</script>
<template>
    <TopBarWrapper>
        <LogoIcon></LogoIcon>

        <!-- <form action="/search" method="POST">
				<input type="text" style="width: 20rem; border: #0db1a4; height: 2.2rem;" class="p-1 px-2 rounded-3 " placeholder="SEARCH" name="search">
        </form> -->

        <div class="flex-inline">
          <SearchBar></SearchBar>
          <router-link to="/login"><button class="btn btn-primary " >LOGIN</button></router-link>
          <router-link to="/signup"><button class="btn btn-primary ">SIGN UP</button></router-link>
        </div>
        
    </TopBarWrapper>

</template>

<style scoped>
.flex-inline{
	display: inline-flex;
	gap:10px
}
</style>