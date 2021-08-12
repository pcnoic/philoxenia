<template>
  <q-layout view="lHh Lpr lFf">
    <div class="q-pa-md">
      <q-toolbar class="bg-purple text-white shadow-2 rounded-borders">
        <q-btn
          to="/"
          flat
          style="font-family: 'Pacifico', cursive"
          label="🏡 Philoxenia"
        />
        <q-space />

        <!--
        notice shrink property since we are placing it
        as child of QToolbar
      -->
        <q-tabs v-model="tab" shrink>
          <q-route-tab
            to="/offer"
            style="font-family: 'Fredoka One', cursive"
            name="offer"
            label="Offer space"
          />
          <q-route-tab
            to="/request"
            style="font-family: 'Fredoka One', cursive"
            name="tab2"
            label="Request space"
          />
          <q-route-tab
            to="/about"
            style="font-family: 'Fredoka One', cursive"
            name="tab3"
            label="About"
          />
        </q-tabs>
      </q-toolbar>
    </div>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { ref } from 'vue';

export default {
  name: 'MainLayout',

  setup() {
    return {
      tab: ref(''),
    };
  },
};
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Pacifico&display=swap');
</style>
