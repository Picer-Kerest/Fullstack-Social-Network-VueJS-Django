<template>
  <div class="max-w-7xl mx-auto grid grid-cols-3 gap-4">

    <div class="main-center col-span-2 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
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
import Toast from '../components/Toast.vue'

export default {
  name: "Feed",
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
    Toast,
  },
  data: () => ({
    posts: [],
    body: '',
  }),
  mounted() {
    this.getFeed()
  },
  methods: {
    getFeed() {
      axios.get('/api/posts/')
          .then(response => {
            console.log('Data is: ', response.data)

            this.posts = response.data
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
            // Добавляем элемент в начало массива
            this.body = ''
          })
          .catch(error => {
            console.log('Error', error)
          })
    },
  },
}

</script>

<style scoped>

</style>