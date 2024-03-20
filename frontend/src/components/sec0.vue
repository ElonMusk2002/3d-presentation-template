<template>
    <div class="video-section">
      <video autoplay muted loop class="video-background">
        <source src="src/components/video/main.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Sec0'
  }
  </script>
  
  <style scoped>
  .video-section {
    width: 100%;
    height: 100vh;
  }
  
  .video-background {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  </style>
  