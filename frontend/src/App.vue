<template>
  <div id="app">
    <div class="content">
      <Sec0 />
      <Sec1 />
      <Sec2 />
      <Sec3 />
      <Sec4 />
      <Sec5 />
      <Sec6 />
      <Sec7 />
      <Sec8 />
      <Sec9 />
    </div>
  </div>
</template>

<script>
import Sec0 from './components/Sec0.vue';
import Sec1 from './components/Sec1.vue';
import Sec2 from './components/Sec2.vue';
import Sec3 from './components/Sec3.vue';
import Sec4 from './components/Sec4.vue';
import Sec5 from './components/Sec5.vue';
import Sec6 from './components/Sec6.vue';
import Sec7 from './components/Sec7.vue';
import Sec8 from './components/Sec8.vue';
import Sec9 from './components/Sec9.vue';

export default {
  components: {
    Sec0,
    Sec1,
    Sec2,
    Sec3,
    Sec4,
    Sec5,
    Sec6,
    Sec7,
    Sec8,
    Sec9,
  },
  mounted() {
    window.addEventListener('keydown', this.toggleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('keydown', this.toggleScroll);
  },
  methods: {
    toggleScroll(event) {
      if (event.key === 'z' || event.key === 'Z') {
        const content = document.querySelector('.content');
        if (content.style.overflowY === 'hidden') {
          content.style.overflowY = 'auto';
        } else {
          content.style.overflowY = 'hidden';
        }
      }
    },
  },
};
</script>

<style>
body,
html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1;
  overflow-y: auto;
}
</style>