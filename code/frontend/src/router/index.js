import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/authentication/Login.vue'
import Signup from '@/components/authentication/Signup.vue'
import Index from '@/components/Index.vue'


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

]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: routes
})

export default router
