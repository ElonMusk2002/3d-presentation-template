<template>
  <div class="scene-container">
    <div ref="container" class="full-screen"></div>>
    <div class="scene-overlay">
      <h1 class="title">Business Needs Web Developers</h1>
      <p class="description">The virtual architects of the future, web developers are an integral part of businesses,
        shaping the digital presence and competitiveness of companies.</p>
    </div>
  </div>
</template>

<script>
import * as THREE from 'three';

export default {
  name: 'DotWavesAnimation',
  mounted() {
    this.createScene();
    this.animate();
    window.addEventListener('resize', this.onResize);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.onResize);
  },
  methods: {
    createScene() {
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0xffffff);

      this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      this.camera.position.z = 5;

      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.$refs.container.appendChild(this.renderer.domElement);

      const dotGeometry = new THREE.BufferGeometry();
      const dotVertices = [];

      for (let i = 0; i < 10000; i++) {
        const x = THREE.MathUtils.randFloatSpread(5);
        const y = THREE.MathUtils.randFloatSpread(5);
        const z = THREE.MathUtils.randFloatSpread(5);

        dotVertices.push(x, y, z);
      }

      dotGeometry.setAttribute('position', new THREE.BufferAttribute(new Float32Array(dotVertices), 3));

      const dotMaterial = new THREE.PointsMaterial({ color: 0x000000, size: 0.05 });

      this.dots = new THREE.Points(dotGeometry, dotMaterial);
      this.scene.add(this.dots);
    },
    animate() {
      requestAnimationFrame(this.animate);

      const vertices = this.dots.geometry.attributes.position.array;
      for (let i = 0; i < vertices.length; i += 3) {
        vertices[i] += 0.001 * (0.5 - Math.random());
        vertices[i + 1] += 0.001 * (0.5 - Math.random());
        vertices[i + 2] += 0.001 * (0.5 - Math.random());
      }
      this.dots.geometry.attributes.position.needsUpdate = true;

      this.dots.rotation.x += 0.0001;
      this.dots.rotation.y += 0.0002;

      this.renderer.render(this.scene, this.camera);
    },
    onResize() {
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
    },
  },
};
</script>

<style scoped>
.scene-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.scene-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: rgb(0, 0, 0);
  z-index: 1;
  text-align: center;
  font-size: 2em;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title {
  color: #4a4747;
  font-family: 'Raleway', sans-serif;
  font-size: 62px;
  font-weight: 800;
  line-height: 72px;
  margin: 0 0 24px;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 0.5em;
}

.description {
  color: #ffffff;
  background: #c0392b;
  background: -webkit-linear-gradient(to right, #8e44ad, #c0392b);
  background: linear-gradient(to right, #8e44ad, #c0392b);
  font-size: 25px;
  font-weight: 800;
  line-height: 42px;
  margin: 0 0 24px;
  line-height: 1.5;
}
</style>