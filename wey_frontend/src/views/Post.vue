<template>
  <div class="max-w-7xl mx-auto grid grid-cols-3 gap-4">

    <div class="main-center col-span-2 space-y-4">
      <div class="p-4 bg-white border border-gray-200 rounded-lg" v-if="post.id">
        <FeedItem :post="post" />
      </div>
        <div class="bg-white border border-gray-200 rounded-lg">
          <form v-on:submit.prevent="submitForm" method="POST">
            <div class="p-4">
              <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you think?"></textarea>
            </div>

            <div class="p-4 border-t border-gray-100">
              <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg w-full">Comment</button>
            </div>
          </form>
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
  name: "Post",
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
    Toast,
  },
  data: () => ({
    post: {
      id: null,
      comments: []
    },
    body: '',
  }),
  mounted() {
    this.getPost()
  },
  methods: {
    getPost() {
      axios.get(`/api/posts/${this.$route.params.id}/`)
          .then(response => {
            console.log('Data is: ', response.data)

            this.post = response.data.post
          })
          .catch(error => {
            console.log('Error', error)
          })
    },
    submitForm() {
      axios.post(`/api/posts/${this.$route.params.id}/comment/`, {
        'body': this.body})
          .then(response => {
            console.log('Response Data', response.data)

            this.post.comments.unshift(response.data)
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