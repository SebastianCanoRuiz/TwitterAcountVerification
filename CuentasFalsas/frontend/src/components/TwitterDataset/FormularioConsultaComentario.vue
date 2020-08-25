<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Consultar veracidad cuenta de Twitter basado en un comentario</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">

                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Comentario</label>
                                <div class="col-sm-6">
                                    <textarea name="comentario" class="form-control" placeholder="Ingrese un comentario..." rows="3"></textarea>
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Consultar</b-button>
                                </div>
                            </div>
                        
                        </form>
                    
                    </div>
                </div>
            </div>
        </div>


    </div>

        
    </div>
  
</template>

<script>
export default {};
</script>

<style>
</style>