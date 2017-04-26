function dedup (list){
  if(!list.head){
    return False:
  }
  var current = list.head;
  var current = current.next;
  while(current){
    while(current2 != null){
      if(current.val == current2.val){
        current.next = current2.next;
        current2.next = null;
      }
    }
    current = current.next;
  }
  return list;
}
