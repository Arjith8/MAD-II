import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/authentication/Login.vue'
import Signup from '../components/authentication/Signup.vue'


const routes=[
	{
		path:'/',
	},
	{
		path:'/login',
		component:Login
	},
	{
		path:'/signup',
		component:Signup
	},

]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: routes
})

export default router
