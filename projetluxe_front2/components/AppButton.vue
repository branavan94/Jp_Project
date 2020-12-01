<template>
  <button
    class="button"
    :class="btnStyle"
    v-bind="$attrs"
    v-on="$listeners"><slot /></button>
</template>

<script>
export default {
  name: 'AppButton',
  props: {
    btnStyle: {
      type: String,
      default: ''
    }
  }
}
</script>


<style scoped>
.button {
  font: inherit;
  background-color: #FFD400;
  color: white;
  padding: 5px;
  cursor: pointer;
  border: 1px solid #FFD400;
  border-radius: 3px;
}
.button:hover,
.button:active {
  background-color: yellow;
  border: 1px solid yellow;
}
.inverted {
  background-color: white;
  color: black;
  border: 1px solid transparent;
}
.inverted:hover,
.inverted:active {
  color: #ccc;
  background-color: white;
  border: 1px solid transparent;
}
.cancel {
  background-color: #C9C9C9;
  color: white;
  border: 1px solid transparent;
}
.cancel:hover,
.cancel:active {
  background-color: grey;
  border: 1px solid transparent;
  color: white;
}
</style>
