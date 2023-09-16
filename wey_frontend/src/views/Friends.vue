<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">

        <p><strong>{{ user.name }}</strong></p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">182 friends</p>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>

      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4" v-if="friendshipRequests.length">
        <div class="p-4 text-center bg-gray-100 rounded-lg" v-for="friend in friendshipRequests" :key="user.id">
          <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">

          <p>
            <strong>
              <RouterLink :to="{ name: 'profile', params: { id: friend.id } }">
                {{ friend.name }}
              </RouterLink>
            </strong>
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>

      <hr>


    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue"
import Trends from "../components/Trends.vue"
import FeedItem from '../components/FeedItem.vue'
import {mapActions, mapGetters} from "vuex"

export default {
  name: "Friends",
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
  },
  mounted() {
    this.getFriends()
  },
  data: () => ({
    user: {},
    friendshipRequests: [],
    friends: [],
  }),
  methods: {
    getFriends() {
      axios.get(`/api/friends/${this.$route.params.id}/`)
          .then(response => {
            console.log('Data is: ', response.data)

            this.friendshipRequests = response.data.requests
            this.friends = response.data.friends
            this.user = response.data.user
          })
          .catch(error => {
            console.log('Error', error)
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