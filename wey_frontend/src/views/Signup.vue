<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Sign up</h1>

        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
        </p>

        <p class="font-bold">
          Already have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here</RouterLink> to log in!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>Name</label><br>
            <input type="text" v-model="form.name" placeholder="Your full name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <div>
            <label>E-mail</label><br>
            <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <div>
            <label>Password</label><br>
            <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <div>
            <label>Repeat password</label><br>
            <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" :key="error">
                {{ error }}
              </p>
            </div>
          </template>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <Toast/>
</template>

<script>
import axios from "axios";
import {mapActions, mapGetters} from "vuex"
import Toast from '../components/Toast.vue'

export default {
  name: "Signup",
  components: {
    Toast
  },
  data: () => ({
    form: {
      email: '',
      name: '',
      password1: '',
      password2: '',
    },
    errors: [],

  }),
  methods: {
    ...mapActions('toast', ['showToast', ]),
    ...mapActions('user', ['setToken', ]),
    submitForm() {
      // Форма соответствует backend форме - SignupForm
      this.errors = []

      if (this.form.email === '') {
        this.errors.push('Your email is missing')
      }

      if (this.form.name === '') {
        this.errors.push('Your name is missing')
      }

      if (this.form.password1.length < 9) {
        this.errors.push('The password is too short')
      }

      if (this.form.password1 === '') {
        this.errors.push('Your password is missing')
      }

      if (this.form.password1 !== this.form.password2) {
        this.errors.push("Passwords don't match")
      }

      if (this.errors.length === 0) {
        axios.post('/api/signup/', this.form)
            .then(response => {
              if (response.data.message === 'success') {
                const new_user_id = response.data.user.id
                // this.showToast({
                //   duration: 5000,
                //   message: 'The user is registered. Please log in',
                //   style: 'bg-emerald-500'})

                axios.post('/api/login/', {
                  email: this.form.email,
                  password: this.form.password1,
                })
                    .then(response => {
                      this.setToken(response.data)
                      axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                      this.$router.push({ name: 'profile', params: { id: new_user_id }})
                      this.showToast({
                        duration: 5000,
                        message: 'The user is registered. Please log in',
                        style: 'bg-emerald-500'})
                    })
                    .catch(error => {
                      console.log('Error ', error)
                    })

                this.form.email = ''
                this.form.name = ''
                this.form.password1 = ''
                this.form.password2 = ''
                // this.$router.push({ name: 'login' })
              } else {
                console.log('Not success toast')
                this.showToast({
                  duration: 5000,
                  message: 'Something went wrong. Please try again',
                  style: 'bg-red-300'})
              }
            })
            .catch(error => {
              console.log('Error ', error)
            })
      }
    }
  },
}
</script>

<style scoped>

</style>