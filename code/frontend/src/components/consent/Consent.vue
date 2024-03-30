<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const token = ref('')
const isChecked = ref('false')
const router = useRouter()

onMounted(()=>{
    token.value = sessionStorage.getItem('MusicalToken')
})
async function upgrade(){
    if (isChecked){
        const response = await fetch('http://127.0.0.1:5000/api/v1/creator_upgrade',{
            method:"POST",
            headers:{
                'Content-Type': 'application/json',
                'Authorization' : token.value
            }
        })
        const data = await response.json()
        if (data.success){
            alert('You have been upgraded to a creator')
            router.push('/creator_menu')
        }
        else{
            alert('You could not be upgraded to a creator')
        }
    }
    
}
</script>


<template>
    <div class="p-2">

        <h1 class="text-center text-white">CREATOR LISENSE</h1>
        <h2 class="text-center text-white">Content Creator Consent Statement</h2>

    </div>
    <div class="text-white">
        <div  class="px-5 pt-2">
            
            <h3 >Introduction</h3>
            <p>
                Welcome to Musical, a creative platform where we celebrate and showcase the talents of content creators like you. We're excited to have you join our community and contribute your unique content. Before you begin, please take a moment to familiarize yourself with our Content Creator Consent Statement. By sharing your content with us, you agree to the following terms and conditions:
            </p>
        
            <h3>1. Content Submission</h3>
            <p>
                At Musical, we believe in the power of creativity and expression. By submitting your content to us, you grant us the non-exclusive right to use, reproduce, distribute, and display the content that you create and submit (the "Content"). This includes, but is not limited to, text, images, audio, video, and any other form of digital media.
            </p>
        
            <h3>2. Ownership</h3>
            <p>
                We respect and acknowledge your ownership of the Content. While you grant us the right to use the Content as described in this statement, you retain full ownership of your creative work. We will never claim ownership of your Content.
            </p>
        
            <h3>3. Usage Rights</h3>
            <p>
                By sharing your Content with us, you allow Musical to use the Content for a variety of purposes:
            </p>
            <ul>
                <li>Displaying your Content proudly on our website and across our social media platforms.</li>
                <li>Utilizing the Content in promotional and marketing materials that celebrate your creativity and our shared community.</li>
                <li>Sharing your Content with our audience, fostering engagement, and showcasing your talents to a wider audience.</li>
            </ul>
        
            <h3>4. Attribution and Recognition</h3>
            <p>
                We value and recognize the hard work and creativity of content creators like you. Whenever we use your Content, we will provide proper attribution, ensuring that you receive the recognition you deserve as the creator.
            </p>
        
            <h3>5. Content Review and Feedback</h3>
            <p>
                We take great care in reviewing and appreciating the Content you submit. Our team will evaluate your Content and provide feedback when necessary. We strive to maintain a collaborative and supportive environment.
            </p>
        
            <h3>6. Compensation</h3>
            <p>
                While contributing to Musical is an opportunity to showcase your talent and reach a wider audience, please note that compensation for the use of Content may vary. Specific compensation details will be discussed on a case-by-case basis, and any agreed-upon compensation terms will be outlined in a separate agreement.
            </p>
        
            <h3>7. Confidentiality</h3>
            <p>
                We respect your trust and will not disclose any confidential or sensitive information related to your Content without your express permission.
            </p>
        
            <h3>8. Termination of Consent</h3>
            <p>
                You have the right to terminate this consent at any time by notifying us in writing. Upon termination, we will promptly remove your Content from our platforms.
            </p>
        
            <h3>9. Exclusivity</h3>
            <p>
                This agreement does not require exclusivity. You are free to share your Content on other platforms and retain the rights to do so.
            </p>
        
            <h3>10. Revocability</h3>
            <p>
                You may revoke this consent at any time for any Content that has not been used. Revocation will not affect any Content already used in compliance with this agreement.
            </p>
        
            <h3>11. User Engagement</h3>
            <p>
                By sharing your Content with us, you agree to engage with our audience and respond to comments and interactions related to your Content as deemed appropriate by Musical.
            </p>
        
            <h3>12. Amendment</h3>
            <p>
                This Content Creator Consent Statement may be amended by Musical with notice to you. Your continued submission of Content will constitute your acceptance of any amendments.
            </p>
        
            <h3>13. Dispute Resolution</h3>
            <p>
                Any disputes arising from this agreement will be resolved through arbitration, following the rules of the [Arbitration Organization]. The decision of the arbitrator(s) shall be final and binding.
            </p>
        
                    
            <h3>Agreement</h3>
            <p>
                By sharing your Content with Musical, you acknowledge that you have read and understood this Content Creator Consent Statement and agree to its terms and conditions.
            </p>
        
            <h3>Contact Information</h3>
            <p>If you have any questions, concerns, or require further clarification about this Content Creator Consent Statement, please feel free to contact us at <span class="text-primary">musical.help@example.com</span>.</p>



            <div class="p-5 pb-3">
                <input type="checkbox" required class="" name="consent" v-model="isChecked">
                <label for="consent">I ACCEPT THE ABOVE CONDITIONS</label>
            </div>
            <div class="p-5 pt-0 ">
                <button class="btn btn-primary" @click="upgrade">SUBMIT</button>
            </div>
        </div>
    </div>
</template>