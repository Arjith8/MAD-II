import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/authentication/Login.vue'
import Signup from '@/components/authentication/Signup.vue'
import Index from '@/components/Index.vue'
import Consent from '@/components/consent/Consent.vue'
import AdminLogin from '@/components/authentication/AdminLogin.vue'
import Logout from '@/components/authentication/Logout.vue'
import Profile from '@/components/profile/Profile.vue'
import SongPage from '@/components/DataViews/SongPage.vue'
import AddLyrics from '@/components/AddLyrics.vue'
import RateSongs from '@/components/RateSongs.vue'
import LyricsPage from '@/components/DataViews/LyricsPage.vue'
import ListSongsCreator from '@/components/ListData/ListSongsCreator.vue'
import ListSongsAlbums from '@/components/ListData/ListSongsAlbums.vue'
import CreatePlaylists from '@/components/CreatePlaylists.vue'
import SeeAll from '@/components/seeAll/SeeAll.vue'
import PlaylistView from '@/components/PlaylistView.vue'
import ListSongsPlaylist from '@/components/ListData/ListSongsPlaylist.vue'
import CreatorDashboard from '@/components/dashboards/CreatorDashboard.vue'
import SongUpload from '@/components/upload/SongUpload.vue'
import EditSong from '@/components/EditSong.vue'
import CreateAlbum from '@/components/CreateAlbum.vue'
import EditAlbum from '@/components/EditAlbum.vue'
import EditLyrics from '@/components/EditLyrics.vue'
import AdminDashboard from '@/components/dashboards/AdminDashboard.vue'
import SearchPage from '@/components/SearchPage.vue'
import Flags from '@/components/Flags.vue'


const routes=[
	{
		path:'/',
		component:Index
	},
	{
		path:'/login',
		component:Login
	},
	{
		path:'/signup',
		component:Signup
	},
	{
		path:'/consent',
		component:Consent
	},
	{
		path:"/hjkksv",
		component: AdminLogin
	},
	{
		path:"/logout",
		component : Logout
	},
	{
		path:'/seemore/:content',
		component: SeeAll
	},
	{
		path : '/song/:id',
		component : SongPage
	},
	{
		path:'/profile',
		component:Profile
	},
	{
		path:"/add_lyrics",
		component: AddLyrics
	},
	{
		path:'/rating',
		component:RateSongs
	},
	{
		path:'/lyrics/:id',
		component:LyricsPage
	},
	{
		path:'/creator/:id',
		component: ListSongsCreator
	},
	{
		path:'/album/:id',
		component: ListSongsAlbums
	},
	{
		path:'/create_playlist',
		component: CreatePlaylists
	},
	{
		path:"/playlists",
		component:PlaylistView
	},
	{
		path:'/playlist/:id',
		component:ListSongsPlaylist
	},
	{
		path:"/creator_menu",
		component:CreatorDashboard
	},
	{
		path:"/song_upload",
		component:SongUpload
	},
	{
		path:"/edit_song/:id",
		component:EditSong
	},
	{
		path:"/create_album",
		component:CreateAlbum
	},
	{
		path:"/edit_album/:id",
		component:EditAlbum
	},
	{
		path:'/edit_lyrics/:id',
		component:EditLyrics
	},
	{
		path:'/admin_menu',
		component:AdminDashboard
	},
	{
		path:'/search/:keyword',
		component:SearchPage
	},
	{
		path:'/flags',
		component:Flags
	}

]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: routes
})

export default router
