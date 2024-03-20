<template>
  <div class="scene-container">
    <Renderer ref="renderer" resize :orbit-ctrl="{ enableDamping: true, dampingFactor: 0.05, autoRotate: true }" shadow>
      <Camera :position="{ y: 100, z: 100 }" />
      <Scene>
        <SpotLight color="#ffffff" :intensity="0.5" :position="{ y: 150, z: 0 }" :cast-shadow="true"
          :shadow-map-size="{ width: 1024, height: 1024 }" />
        <SpotLight color="#ff0000" :intensity="0.5" :position="{ y: -150, z: 0 }" :cast-shadow="true"
          :shadow-map-size="{ width: 1024, height: 1024 }" />
        <InstancedMesh ref="imesh" :count="NUM_INSTANCES" :cast-shadow="true" :receive-shadow="true">
          <SphereGeometry :radius="5" />
          <PhongMaterial />
        </InstancedMesh>
      </Scene>
      <EffectComposer>
        <RenderPass />
        <UnrealBloomPass :strength="2" />
      </EffectComposer>
    </Renderer>
    <div class="scene-overlay">
      <h1>Web Developer</h1>
      <p>The most creative and exciting profession in IT</p>
    </div>
  </div>
</template>

<script>
import { Object3D, MathUtils } from 'three';

import {
  Camera,
  EffectComposer,
  InstancedMesh,
  PhongMaterial,
  Renderer,
  RenderPass,
  SphereGeometry,
  SpotLight,
  Scene,
  UnrealBloomPass,
} from 'troisjs';

export default {
  components: {
    Camera,
    EffectComposer,
    InstancedMesh,
    PhongMaterial,
    Renderer,
    RenderPass,
    SphereGeometry,
    SpotLight,
    Scene,
    UnrealBloomPass,
  },
  setup() {
    return {
      NUM_INSTANCES: 2000,
    };
  },
  mounted() {
    const imesh = this.$refs.imesh.mesh;
    const dummy = new Object3D();
    const { randFloat: rnd, randFloatSpread: rndFS } = MathUtils;
    for (let i = 0; i < this.NUM_INSTANCES; i++) {
      dummy.position.set(rndFS(200), rndFS(200), rndFS(200));
      const scale = rnd(0.2, 1);
      dummy.scale.set(scale, scale, scale);
      dummy.updateMatrix();
      imesh.setMatrixAt(i, dummy.matrix);
    }
    imesh.instanceMatrix.needsUpdate = true;
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
  color: white;
  z-index: 1;
  text-align: center;
  font-size: 2em;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.scene-overlay h1 {
  color: #ffffff;
  font-family: 'Raleway', sans-serif;
  font-size: 72px;
  font-weight: 800;
  line-height: 72px;
  margin: 0 0 24px;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 0.5em;
}

.scene-overlay p {
  color: #f8f8f8;
  font-family: 'Raleway', sans-serif;
  font-size: 35px;
  font-weight: 500;
  line-height: 32px;
  margin: 0 0 24px;
  line-height: 1.5;
}
</style>