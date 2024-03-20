<template>
  <div class="ai-web-development-page">
    <section class="hero">
      <div class="hero-content">
        <h1>AI + Web Development</h1>
        <p>Use LLAMA to create intelligent web applications</p>
      </div>
    </section>

    <div class="benefits">
      <div class="benefit-card">
        <div class="icon">
          <font-awesome-icon icon="code" />
        </div>
        <div class="text">
          <h3>Faster Development</h3>
          <p>LLAMA allows for rapid prototyping and development, reducing time to market for your web applications. With
            automation and intelligent algorithms, you can focus on creating unique content and functionality rather
            than routine tasks.</p>
        </div>
      </div>

      <div class="benefit-card">
        <div class="icon">
          <font-awesome-icon icon="rocket" />
        </div>
        <div class="text">
          <h3>Better Code Completion</h3>
          <p>LLAMA offers advanced context-based code completion features, helping developers write code more
            efficiently and accurately. This speeds up the development process and improves code quality, making it more
            readable and maintainable.</p>
        </div>
      </div>

      <div class="benefit-card">
        <div class="icon">
          <font-awesome-icon icon="brain" />
        </div>
        <div class="text">
          <h3>More Maintainable Code</h3>
          <p>LLAMA provides insights into code structure and best practices, assisting developers in writing cleaner and
            more maintainable code. This not only improves code quality but also facilitates its support and extension
            in the future.</p>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
}

.container {
  width: 90%;
  margin: 0 auto;
}

.ai-web-development-page {
  background-color: #1a1a1a;
  color: #fff;
}

.hero {
  height: 100vh;
  background-image: url('https://images.unsplash.com/photo-1488554378835-f7acf46e6c98?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
  /* Replace with your high-quality image */
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
}

.hero h1 {
  font-size: 7rem;
}

.hero p {
  font-size: 3.5rem;
}

.benefits {
  padding: 50px 0;
}

.benefit-card {
  display: flex;
  margin-bottom: 30px;
}

.icon {
  flex: 0 0 100px;
  font-size: 2rem;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.text {
  margin-left: 20px;
}

.text h3 {
  font-size: 1.5rem;
}

.text p {
  font-size: 1.1rem;
}
</style>