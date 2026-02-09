<script setup lang="ts">
import { ref } from 'vue'
import { useShoppingListsStore } from '@/stores/shopping-lists'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Button from 'primevue/button'

const visible = defineModel<boolean>('visible', { required: true })

const store = useShoppingListsStore()
const name = ref('')
const description = ref('')
const submitting = ref(false)

async function submit() {
    if (!name.value.trim()) return
    submitting.value = true
    try {
        await store.createList(name.value.trim(), description.value.trim() || undefined)
        name.value = ''
        description.value = ''
        visible.value = false
    } finally {
        submitting.value = false
    }
}
</script>

<template>
    <Dialog
        v-model:visible="visible"
        header="Create New List"
        modal
        :style="{ width: '28rem' }"
        :closable="true"
    >
        <div class="dialog-form">
            <div class="form-field">
                <label for="list-name">Name</label>
                <InputText
                    id="list-name"
                    v-model="name"
                    placeholder="e.g. Weekly Groceries"
                    fluid
                    @keyup.enter="submit"
                />
            </div>
            <div class="form-field">
                <label for="list-desc">Description (optional)</label>
                <Textarea
                    id="list-desc"
                    v-model="description"
                    placeholder="What's this list for?"
                    rows="3"
                    fluid
                    style="resize: none"
                />
            </div>
        </div>
        <template #footer>
            <Button label="Cancel" text @click="visible = false" />
            <Button label="Create" :loading="submitting" :disabled="!name.trim()" @click="submit" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss" src="@/assets/styles/components/_create-list-dialog.scss"></style>
