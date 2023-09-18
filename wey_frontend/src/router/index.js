import { createRouter, createWebHistory } from 'vue-router'
// import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import HomeView from '@/views/Home.vue'
import AboutView from "@/views/About.vue"
import Signup from "@/views/Signup.vue"
import Login from "@/views/Login.vue";
import Feed from "@/views/Feed.vue";
import Messages from "@/views/Messages.vue";
import Search from "@/views/Search.vue";
import Profile from "@/views/Profile.vue";
import Friends from "@/views/Friends.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {path: '/', name: 'home', component: HomeView},
        {path: '/about', name: 'about', component: AboutView},
        {path: '/signup', name: 'signup', component: Signup},
        {path: '/profile/:id', name: 'profile', component: Profile},
        {path: '/profile/:id/friends', name: 'friends', component: Friends},
        {path: '/login', name: 'login', component: Login},
        {path: '/feed', name: 'feed', component: Feed},
        {path: '/messages', name: 'messages', component: Messages},
        {path: '/search', name: 'search', component: Search},
    ]
})


// const routes = [
//     {path: '/', name: 'home', component: HomeView},
//     {path: '/about', name: 'about', component: AboutView},
//     {path: '/signup', name: 'signup', component: Signup},
//     {path: '/profile/:id', name: 'profile', component: Profile},
//     {path: '/profile/:id/friends', name: 'friends', component: Friends},
//     {path: '/login', name: 'login', component: Login},
//     {path: '/feed', name: 'feed', component: Feed},
//     {path: '/messages', name: 'messages', component: Messages},
//     {path: '/search', name: 'search', component: Search},
// ]
//
//
// const router = createRouter({
//   history: createWebHashHistory(),
//   routes
// })

export default router