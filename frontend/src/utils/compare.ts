export function compareCatItems(a:any, b:any){
    if(a.items > b.items) return -1
    else if(a.items < b.items) return 1
    else return 0
}