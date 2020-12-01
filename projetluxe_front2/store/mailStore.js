import vuex from 'vuex';


/*This is the data, what we want to conserve*/
export const state = () => {
  inbox: [];
  drafts:[];
  sent:[];
  draftToModify:{};
}


/*Here the functions we want to commit*/
export const mutations = {
  setInbox(state, inbox) {
    state.inbox = inbox ;
  },
  setDrafts(state, drafts) {
    state.drafts = drafts ;
  },
  setSent(state, sent) {
    state.sent = sent ;
  },
  addDraft(state, draft){
    var drafts = state.drafts;
    drafts.push(draft);
    state.drafts = drafts ;
  },
  modifyDraft(state, draft){
    var drafts = state.drafts;
    //var oldDraft = drafts.filter(e => e.id === draft.id)
    for( var i = 0; i < drafts.length; i++){
       if ( drafts[i].id === draft.id) {
         state.drafts.splice(i, 1);
       }
    }
    state.drafts.push(draft);
    state.drafts = drafts ;
  },
  setDraftM(state, draft) {
    state.draftToModify = draft ;
  }

}
