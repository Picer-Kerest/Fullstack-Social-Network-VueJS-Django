<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">

        <p><strong>{{ user.name }}</strong></p>

        <div class="mt-6 flex space-x-8 justify-around">
          <RouterLink :to="{ name: 'friends', params: { id: getId } }" class="text-xs text-gray-500">{{ user.friends_count }} friends</RouterLink>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>

        <div class="mt-6">
          <button
              class="inline-block py-4 px-3 bg-purple-600 text-sm text-white rounded-lg w-full"
              v-if="getId !== user.id"
              @click="sendFriendshipRequest"
          >
            Send friendship request
          </button>

          <button
              class="inline-block py-4 px-3 bg-red-600 text-sm text-white rounded-lg w-full"
              v-if="getId === user.id"
              @click="logout"
          >
            Logout
          </button>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg" v-if="getId === user.id">
        <form v-on:submit.prevent="submitForm" method="POST">
          <div class="p-4">
            <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
          </div>

          <div class="p-4 border-t border-gray-100 flex justify-between">
            <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

            <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
          </div>
        </form>
      </div>


      <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" :key="post.id">
        <FeedItem :post="post" />
      </div>

    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
  <Toast/>
</template>

<script>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue"
import Trends from "../components/Trends.vue"
import FeedItem from '../components/FeedItem.vue'
import {mapActions, mapGetters} from "vuex"
import Toast from '../components/Toast.vue'

export default {
  name: "Profile",
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
    Toast,
  },
  data: () => ({
    posts: [],
    user: {},
    body: '',
  }),
  mounted() {
    this.getFeed()
  },
  watch: {
    '$route.params.id': {
      handler: function() {
        this.getFeed()
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    ...mapActions('toast', ['showToast', ]),
    ...mapActions('user', ['removeToken', ]),
    sendFriendshipRequest() {
      axios.post(`api/friends/${this.$route.params.id}/request/`)
          .then(response => {
            console.log('Data is: ', response.data)

            if (response.data.message === 'friendship request already sent') {
              this.showToast({
                duration: 5000,
                message: 'The request has already been sent',
                style: 'bg-red-300'
              })
            } else {
              this.showToast({
                duration: 5000,
                message: 'The request was sent',
                style: 'bg-emerald-500'
              })
            }

          })
          .catch(error => {
            console.log('Error', error)
          })
    },
    getFeed() {
      axios.get(`/api/posts/profile/${this.$route.params.id}/`)
          .then(response => {
            this.posts = response.data.posts
            this.user = response.data.user
          })
          .catch(error => {
            console.log('Error', error)
          })
    },
    submitForm() {
      console.log('SubmitForm. Body is: ', this.body)
      axios.post('/api/posts/create/', {
        'body': this.body})
          .then(response => {
            console.log('New post From Back: ', response.data)
            this.posts.unshift(response.data)
            this.body = ''
          })
          .catch(error => {
            console.log('Error', error)
          })
    },
    logout() {
      console.log('Logout')
      this.removeToken()
      this.$router.push({name: 'login'})
      this.showToast({
        duration: 5000,
        message: 'Success logout',
        style: 'bg-emerald-500'
      })
    }
  },
  computed: {
    ...mapGetters('user', ['getName', 'getId']),
  }
}

</script>

<style scoped>

</style>