<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
sessionStorage.removeItem('MusicalToken')
router.push('/')
</script>