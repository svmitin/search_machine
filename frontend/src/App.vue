<template lang="pug">
    #app
        keep-alive(:include="['Sites']")
            router-view
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    computed: {
        ...mapGetters('Publisher', ['isAuthorized']),
    },
    methods: {
        ...mapActions('Publisher', ['logout', 'getPubInfo']),
        ...mapActions('Refbooks', ['fetchRefbooks']),
        ...mapActions('Sites', ['fetchSites']),
        ...mapActions('Statistics', ['getIncomeByPeriod']),
    },
    watch: {
        isAuthorized(newVal) {
            if (newVal) {
                this.getPubInfo()
                this.fetchRefbooks()
                this.fetchSites({
                    lastSiteId: 0,
                    status: '',
                    url: '',
                })
                this.getIncomeByPeriod()
            }
        },
    },
}
</script>

<style lang="stylus">

#app
    font-family 'Open Sans', Avenir, Helvetica, Arial, sans-serif
    -webkit-font-smoothing antialiased
    -moz-osx-font-smoothing grayscale
    background-color #e7ebee
</style>
