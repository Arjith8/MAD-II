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
        <LogoIcon />

        <SearchBar />

        <div class="nav">
            <li class="nav-item ">
                <a href="/admin_page/flags" class="nav-link active text-primary   ">FLAGS</a>
            </li>
            <li class="nav-item ">
                <a href="/admin_page/blacklisted" class="nav-link active text-primary  ">BLACKLISTS</a>
            </li>
            <li class="nav-item ">
                <RouterLink to="/logout" class="nav-link active logout">LOGOUT</RouterLink>
            </li>
        </div>

    </TopBarWrapper>
</template>