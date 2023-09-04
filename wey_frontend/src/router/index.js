import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import HomeView from '@/views/Home.vue'
import AboutView from "@/views/About.vue"
import Signup from "@/views/Signup.vue"
import Login from "@/views/Login.vue";
import Feed from "@/views/Feed.vue";
import Messages from "@/views/Messages.vue";
import Search from "@/views/Search.vue";
import Profile from "@/views/Profile.vue";


const routes = [
    {path: '/', name: 'home', component: HomeView},
    {path: '/about', name: 'about', component: AboutView},
    {path: '/signup', name: 'signup', component: Signup},
    {path: '/profile/:id', name: 'profile', component: Profile},
    {path: '/login', name: 'login', component: Login},
    {path: '/feed', name: 'feed', component: Feed},
    {path: '/messages', name: 'messages', component: Messages},
    {path: '/search', name: 'search', component: Search},
]


const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router