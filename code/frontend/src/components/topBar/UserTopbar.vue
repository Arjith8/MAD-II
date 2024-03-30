<script setup>
import { defineProps } from 'vue';

import TopBarWrapper from '@/components/wrappers/TopBarWrapper.vue';
import LogoIcon from "@/components/icons/IconLogo.vue";
import SearchBar from '@/components/searchBar/SearchBar.vue';
import { RouterLink } from 'vue-router';

defineProps(["logged"])

</script>
<template>
    <TopBarWrapper>
        <LogoIcon></LogoIcon>

        <div class="flex-inline">
			<SearchBar></SearchBar>

			<router-link to="/login" v-if="!logged"><button class="btn btn-primary " >LOGIN</button></router-link>
			<router-link to="/signup" v-if="!logged"><button class="btn btn-primary ">SIGN UP</button></router-link>

			<div class="nav" v-else>
				<li class="nav-item ">
				<RouterLink to="/creator_menu" class="nav-link active creator">CREATOR</RouterLink>
				</li>
				<li class="nav-item ">
				<RouterLink to="/playlists" class="nav-link active account">PLAYLISTS</RouterLink>
				</li>
				<li class="nav-item">
				<RouterLink to="/profile" class="nav-link active creator">PROFILE</RouterLink>
				</li>
				<li class="nav-item ">
				<RouterLink to="/logout" class="nav-link active logout">LOGOUT</RouterLink>
				</li>
			</div>

        </div>
        
    </TopBarWrapper>

</template>

<style scoped>
.flex-inline{
	display: inline-flex;
	gap:10px
}
</style>