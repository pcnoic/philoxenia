<template>
  <q-page class="column items-center justify-evenly">
    <h2 class="text-center">If you are a space owner, fill the form.</h2>
    <div class="q-pa-md" style="max-width: 400px">
      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input
          filled
          v-model="name"
          label="Your name *"
          hint="Name and surname"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Please type something']"
        />

        <q-input
          filled
          type="number"
          v-model="age"
          label="Your age *"
          hint="Your age. Eg: 25"
          lazy-rules
          :rules="[
            (val) => (val !== null && val !== '') || 'Please type your age',
            (val) => (val > 0 && val < 100) || 'Please type a real age',
          ]"
        />

        <q-select
          standout
          v-model="spacetype"
          :options="options"
          label="Space Type"
        />

        <q-badge color="secondary">
          Max visitors: {{ visitorscount }}
        </q-badge>

        <q-slider
          v-model="visitorscount"
          :min="1"
          :max="15"
          :step="1"
          label="Visitors"
          label-always
          color="light-green"
        />

        <div class="q-pa-md">
          <q-checkbox v-model="pet" label="Pet Friendly" />
        </div>

        <div class="q-pa-md">
          <q-date subtitle="Availability" v-model="timeperiod" range />
        </div>

        <q-toggle v-model="accept" label="I accept the conditions." />

        <div>
          <q-btn label="Submit" type="submit" color="primary" />
          <q-btn
            label="Reset"
            type="reset"
            color="primary"
            flat
            class="q-ml-sm"
          />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import { useQuasar } from 'quasar';
import { ref } from 'vue';

export default {
  setup() {
    const $q = useQuasar();

    const name = ref(null);
    const age = ref(null);
    const accept = ref(false);

    return {
      visitorscount: ref(1),
      spacetype: ref(null),
      options: [
        'Flat',
        'Condo',
        'Single-Family',
        'Cottage',
        'Villa',
        'Tiny Home',
        'Shared Space',
      ],
      timeperiod: ref({ from: '2020/07/08', to: '2020/07/17' }),
      pet: ref(false),
      name,
      age,
      accept,

      onSubmit() {
        if (accept.value !== true) {
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: 'You need to accept the license and terms first',
          });
        } else {
          $q.notify({
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Submitted',
          });
        }
      },

      onReset() {
        name.value = null;
        age.value = null;
        accept.value = false;
      },
    };
  },
};
</script>
