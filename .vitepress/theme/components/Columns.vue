<template>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div class="column" style="padding: 0px 5px 0px 0px; border-radius: 8px;">
      <slot name="left">
      </slot>
    </div>
    <div class="column" style="padding: 0px 0px 0px 5px; border-radius: 8px;">
      <slot name="right"> 
      </slot>
    </div>
  </div>
</template>

