<template>
  <div class="scene-container">
    <Renderer ref="renderer" resize antialias
      :orbit-ctrl="{ autoRotate: true, enableDamping: true, dampingFactor: 0.05 }" pointer>
      <Camera :position="{ x: 0, y: 0, z: 10 }" />
      <Scene background="#000000">
        <PointLight ref="light" :intensity="0.5" :position="{ x: 0, y: 0, z: 0 }">
          <Sphere :radius="0.1" />
        </PointLight>
        <Group :rotation="{ x: -Math.PI / 2, y: 0, z: 0 }">
          <RectAreaLight color="#ff6000" :position="{ x: 0, y: 10, z: 1 }" v-bind="rectLightsProps" />
          <RectAreaLight color="#0060ff" :position="{ x: 10, y: 0, z: 1 }" v-bind="rectLightsProps" />
          <RectAreaLight color="#60ff60" :position="{ x: -10, y: 0, z: 1 }" v-bind="rectLightsProps" />
          <RectAreaLight color="#ffffff" :position="{ x: 0, y: -10, z: 1 }" v-bind="rectLightsProps" />
          <Plane :width="30" :height="30" :rotation="{ x: 0 }" :position="{ z: -3 }">
            <StandardMaterial :props="{ displacementScale: 0.2, roughness: 0, metalness: 0 }">
              <Texture :props="texturesProps" src="/assets/textures/Wood_Tiles_002_basecolor.jpg" />
              <Texture :props="texturesProps" src="/assets/textures/Wood_Tiles_002_height.png" name="displacementMap" />
              <Texture :props="texturesProps" src="/assets/textures/Wood_Tiles_002_normal.jpg" name="normalMap" />
              <Texture :props="texturesProps" src="/assets/textures/Wood_Tiles_002_roughness.jpg" name="roughnessMap" />
              <Texture :props="texturesProps" src="/assets/textures/Wood_Tiles_002_ambientOcclusion.jpg" name="aoMap" />
            </StandardMaterial>
          </Plane>
        </Group>
      </Scene>
      <EffectComposer>
        <RenderPass />
        <UnrealBloomPass :strength="0.3" />
        <FXAAPass />
      </EffectComposer>
    </Renderer>
    <div class="scene-overlay">
      <h1>Perspectives</h1>
      <p>In the future, web developers will become masters of virtual reality, creating interactive worlds that blend
        technology, creativity, and human experience.</p>
    </div>
  </div>
</template>

<script>
import { RepeatWrapping } from 'three';
import {
  AmbientLight,
  Camera,
  EffectComposer,
  FXAAPass,
  Group,
  Renderer,
  Plane,
  PointLight,
  RectAreaLight,
  RenderPass,
  Scene,
  Sphere,
  StandardMaterial,
  Texture,
  UnrealBloomPass,
} from 'troisjs';

export default {
  components: {
    AmbientLight,
    Camera,
    EffectComposer,
    FXAAPass,
    Group,
    Renderer,
    Plane,
    PointLight,
    RectAreaLight,
    RenderPass,
    Scene,
    Sphere,
    StandardMaterial,
    Texture,
    UnrealBloomPass,
  },
  data() {
    return {
      texturesProps: {
        repeat: { x: 10, y: 10 },
        wrapS: RepeatWrapping,
        wrapT: RepeatWrapping,
      },
      rectLightsProps: {
        lookAt: { x: 0, y: 0, z: 1 },
        intensity: 5,
        width: 5,
        height: 5,
        helper: true,
      },
    };
  },
  mounted() {
    const renderer = this.$refs.renderer;
    const light = this.$refs.light.light;
    const pointerV3 = renderer.three.pointer.positionV3;
    renderer.onBeforeRender(() => {
      light.position.copy(pointerV3);
    });
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
  font-size: 62px;
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
  font-size: 18px;
  font-weight: 500;
  line-height: 32px;
  margin: 0 0 24px;
  line-height: 1.5;
}
</style>