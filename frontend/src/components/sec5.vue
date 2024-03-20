<template>
  <div class="animated fadeIn">
    <canvas id="developersLineGraph"></canvas>
  </div>
</template>
  
<script>
export default {
  name: 'DevelopersLineGraph',
  data() {
    return {
      chart: null,
      years: [],
      developers: [],
    };
  },
  mounted() {
    this.createChart();
  },
  methods: {
    createChart() {
      const startYear = 2020;
      const endYear = 2024;
      for (let year = startYear; year <= endYear; year++) {
        this.years.push(year);
        const baseDevelopers = year - startYear + 0.25;
        let fluctuation;
        if (year >= endYear - 3) {
          fluctuation = Math.random() * 1000000 - 500000;
        } else {
          fluctuation = Math.random() * 400000 - 200000;
        }
        this.developers.push(baseDevelopers * 1000000 + fluctuation);
      }

      const ctx = document.getElementById('developersLineGraph').getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.years,
          datasets: [{
            label: 'Number of Developers (in millions)',
            data: this.developers.map(dev => dev / 1000000),
            borderColor: '#A9A9A9',
            backgroundColor: 'rgba(169, 169, 169, 0.2)',
          }],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                callback: function (value, index, values) {
                  return value + 'M';
                }
              }
            },
            x: {
              ticks: {
                color: '#A9A9A9',
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                color: '#A9A9A9',
              }
            }
          },
          backgroundColor: 'rgba(30, 30, 30, 0.8)',
          borderColor: '#A9A9A9',
        },
      });
    },
  },
};
</script>
  
<style scoped>
canvas {
  max-width: 100%;
  background-color: rgba(30, 30, 30, 0.8);
}
</style>
  