import { defineStore } from "pinia";

export const useIndexStore = defineStore('index_data', {
  state: () => ({
    songs: {},
    creators: {},
    albums: {},
    favourites:{}
  }),
  actions: {

    async getFavourites(token) {
      const response = await fetch('http://127.0.0.1:5000/api/v1/favourites',{
        method:"GET",
        headers:{
          "Content-Type":'application/json',
          "Authorization":token
        },
      });
      const favourites = await response.json();
      this.favourites = favourites;
    },

    async getSongs() {
      const response = await fetch('http://127.0.0.1:5000/api/v1/songs',{
        headers:{
          "Content-Type":'application/json',
        },
      });
      const songs = await response.json();
      this.songs = songs;
    },

    async getCreators() {
      const response = await fetch('http://127.0.0.1:5000/api/v1/creators',{
        headers:{
          "Content-Type":'application/json',
        },
      });
      const creators = await response.json();
      this.creators = creators;
    },

    async getAlbums() {
      const response = await fetch('http://127.0.0.1:5000/api/v1/albums',{
        headers:{
          "Content-Type":'application/json',
        },
      });
      const albums = await response.json();
      this.albums = albums;
    },

  },

});