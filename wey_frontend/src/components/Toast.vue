<template>
  <div
      v-if="getIsVisible"
      class="transition ease-in-out delay-500 duration-500 px-6 py-6 fixed top-full right-8 rounded-xl shadow-xl"
      :class="getClasses"
  >
    {{ getMessage }}
  </div>
</template>

<script>
import {mapGetters} from "vuex"

export default {
  name: "Toast",
  computed: {
    ...mapGetters('toast', ['getIsVisible', 'getClasses', 'getMessage', ]),
  },
}
</script>

<style scoped>

</style>
