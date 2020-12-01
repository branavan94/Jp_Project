<template lang="html">
  <section>
    <b-row v-if="this.from" class="mail-preview p-1 m-0 align-items-center">
      <b-col cols="1" class="text-left">
        {{from}}
      </b-col>
      <b-col class="text-right">
        {{title}}
      </b-col>
      <b-col lg class="preview overflow-hidden d-none d-sm-block align-self-baseline justify-content-end">
        {{preview}}
      </b-col>
    </b-row>
    <b-row v-else class="mail-preview w-100 p-1 m-0 align-items-center">
      <b-col cols="1" class="text-left">
        {{to}}
      </b-col>
      <b-col class="text-right">
        {{title}}
      </b-col>
      <b-col lg class="preview text-left overflow-hidden d-none d-sm-block align-self-baseline justify-content-end">
        {{preview}}
      </b-col>
    </b-row>
  </section>

</template>

<script>
export default {
  props:{
      from:{
        type: String,
        required:false
      },
      to:{
        type: String,
        required:false
      },
      title:{
        type: String,
        required:true
      },
      preview:{
        type: String,
        required:true
      }

  }
}
</script>

<style lang="css" scoped>
.mail-preview{

}
.preview{
  border-left:1px solid #C9C9C9;
  max-height: 40px;
}
</style>
