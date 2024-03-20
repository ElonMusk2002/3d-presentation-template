<template>
  <div class="scene-container">
    <Renderer ref="renderer" resize orbit-ctrl pointer>
      <Camera :position="{ z: 200 }" />
      <Scene>
        <AmbientLight color="#808080" />
        <PointLight color="#ff6000" />
        <PointLight ref="light" color="#0060ff" :intensity="0.5" />
        <PointLight color="#ff6000" :intensity="0.5" :position="{ x: 100 }" />
        <PointLight color="#0000ff" :intensity="0.5" :position="{ x: -100 }" />

        <InstancedMesh ref="imesh" :count="NUM_INSTANCES">
          <BoxGeometry :width="2" :height="2" :depth="10" />
          <StandardMaterial :props="{ transparent: true, opacity: 0.9, metalness: 0.8, roughness: 0.5 }" />
        </InstancedMesh>

        <Text text="TroisJS" font-src="/assets/helvetiker_regular.typeface.json" align="center" :size="30" :height="5"
          :position="{ x: 0, y: 0, z: 0 }" :cast-shadow="true">
          <PhongMaterial />
        </Text>
      </Scene>
      <EffectComposer>
        <RenderPass />
        <UnrealBloomPass :strength="1" />
        <HalftonePass :radius="1" :scatter="0" />
      </EffectComposer>
    </Renderer>
    <div class="scene-overlay">
      <h1>Who is a web developer?</h1>
      <p><span class="span_web">Web developer</span> - the architect of the online world, creating digital stories with
        creativity and code.</p>
    </div>
  </div>
</template>

<script>
import { Object3D, MathUtils, Vector3 } from 'three';
const { randFloat: rnd, randFloatSpread: rndFS } = MathUtils;

import {
  AmbientLight,
  BoxGeometry,
  Camera,
  EffectComposer,
  HalftonePass,
  InstancedMesh,
  PhongMaterial,
  PointLight,
  Renderer,
  RenderPass,
  StandardMaterial,
  Scene,
  Text,
  UnrealBloomPass,
} from 'troisjs';

export default {
  components: {
    AmbientLight,
    BoxGeometry,
    Camera,
    EffectComposer,
    HalftonePass,
    InstancedMesh,
    PhongMaterial,
    PointLight,
    Renderer,
    RenderPass,
    StandardMaterial,
    Scene,
    Text,
    UnrealBloomPass,
  },
  setup() {
    const NUM_INSTANCES = 2000;
    const instances = [];
    const target = new Vector3();
    const dummyO = new Object3D();
    const dummyV = new Vector3();

    for (let i = 0; i < NUM_INSTANCES; i++) {
      instances.push({
        position: new Vector3(rndFS(200), rndFS(200), rndFS(200)),
        scale: rnd(0.2, 1),
        scaleZ: rnd(0.1, 1),
        velocity: new Vector3(rndFS(2), rndFS(2), rndFS(2)),
        attraction: 0.03 + rnd(-0.01, 0.01),
        vlimit: 1.2 + rnd(-0.1, 0.1),
      });
    }

    return {
      NUM_INSTANCES,
      instances,
      target,
      dummyO,
      dummyV,
    };
  },
  mounted() {
    this.renderer = this.$refs.renderer;
    this.imesh = this.$refs.imesh.mesh;
    this.light = this.$refs.light.light;
    this.init();
  },
  methods: {
    init() {
      for (let i = 0; i < this.NUM_INSTANCES; i++) {
        const { position, scale, scaleZ } = this.instances[i];
        this.dummyO.position.copy(position);
        this.dummyO.scale.set(scale, scale, scaleZ);
        this.dummyO.updateMatrix();
        this.imesh.setMatrixAt(i, this.dummyO.matrix);
      }
      this.imesh.instanceMatrix.needsUpdate = true;

      this.renderer.onBeforeRender(this.animate);
    },
    animate() {
      const { pointer } = this.renderer.three;
      this.target.copy(pointer.positionV3);
      this.light.position.copy(this.target);

      for (let i = 0; i < this.NUM_INSTANCES; i++) {
        const { position, scale, scaleZ, velocity, attraction, vlimit } = this.instances[i];

        this.dummyV.copy(this.target).sub(position).normalize().multiplyScalar(attraction);
        velocity.add(this.dummyV).clampScalar(-vlimit, vlimit);
        position.add(velocity);

        this.dummyO.position.copy(position);
        this.dummyO.scale.set(scale, scale, scaleZ);
        this.dummyO.lookAt(this.dummyV.copy(position).add(velocity));
        this.dummyO.updateMatrix();
        this.imesh.setMatrixAt(i, this.dummyO.matrix);
      }
      this.imesh.instanceMatrix.needsUpdate = true;
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
  top: 0;
  left: 0;
  color: white;
  z-index: 1;
  text-align: left;
  font-size: 2em;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  padding: 1em;
  border-radius: 10px;
}

.scene-overlay h1 {
  font-size: 2.5em;
  margin-bottom: 0.5em;
}

.scene-overlay p {
  position: absolute;
  bottom: 0;
  right: 0;
  font-size: 1.1rem;
  line-height: 1.5;
}

.span_web {
  font-size: 1.5rem;
}
</style>