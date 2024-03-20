<template>
  <section class="salary-section">
    <div class="content-wrapper">
      <div class="content">
        <h2 class="title">About Developers' Salaries</h2>
        <p class="text">
          Developer salaries in ((country)) are competitive: The average developer salary is around $85,000 per year.
          This is significantly higher than in previous years, indicating a growing demand for skilled developers in the
          country.
        </p>
        <p class="text">
          The technology industry in ((country)) is rapidly evolving, and many companies are investing in their
          developer teams to keep up with global technological trends. It is expected that this growth will continue,
          providing more opportunities for developers to advance in their careers and earn higher salaries.
        </p>
        <p class="text">
          Additionally, the government is implementing initiatives to support the technology sector, including tax
          incentives and educational programs. This further stimulates industry growth.
        </p>
        <p class="text">
          With such promising prospects and a favorable developer ecosystem, developers in ((country)) can succeed in
          their careers and contribute to the technological progress of the country.
        </p>
      </div>
      <div class="image-container">
        <div class="image-grid">
          <div class="image-item">
            <img src="../img/data.png" alt="Data Image 1" />
          </div>
          <div class="image-item">
            <img src="../img/data2.png" alt="Data Image 2" />
          </div>
          <div class="image-item">
            <img src="../img/data3.png" alt="Data Image 3" />
          </div>
        </div>
      </div>
    </div>
    <div class="companies-section">
      <h2 class="title">Top Positions for Web Developers</h2>
      <div class="companies-list">
        <div class="company-item">
          <img src="https://example.com" alt="Company 1 Logo" class="company-logo" />
          <div class="company-details">
            <h3 class="company-name">Company 1</h3>
            <p class="company-position">Full Stack Developer</p>
            <p class="company-salary">from $10,000 to $30,000</p>
          </div>
        </div>
        <div class="company-item">
          <img src="https://example.com" alt="Company 2 Logo" class="company-logo" />
          <div class="company-details">
            <h3 class="company-name">Company 2</h3>
            <p class="company-position">Middle Frontend Developer</p>
            <p class="company-salary">from 10000$ to 150000$</p>
          </div>
        </div>
        <div class="company-item">
          <img src="https://example.com" alt="Company 3 Logo" class="company-logo" />
          <div class="company-details">
            <h3 class="company-name">Company 3</h3>
            <p class="company-position">Full Stack Developer</p>
            <p class="company-salary">from $8000 to $16000</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<style scoped>
.salary-section {
  background: linear-gradient(135deg, #1a1a1a, #2e2e2e);
  padding: 2rem 1rem;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.content {
  color: #fff;
  line-height: 1.8;
}

.title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: #fff;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.companies-section {
  padding: 2rem 1rem;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  margin-top: 2rem;
}

.title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: #333;
}

.companies-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.company-item {
  display: flex;
  align-items: center;
}

.company-logo {
  width: 100px;
  height: auto;
  margin-right: 1rem;
}

.company-details {
  display: flex;
  flex-direction: column;
}

.company-name {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.company-position,
.company-salary {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.company-salary {
  font-weight: 600;
}

.text {
  font-size: 1.1rem;
  margin-bottom: 1.rem;
  color: #ddd;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  gap: 1rem;
}

.image-item img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.image-item img:hover {
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .title {
    font-size: 2.5rem;
  }

  .text {
    font-size: 1.1rem;
  }
}
</style>