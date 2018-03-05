import SearchStore from './search';

export default class Stores {
  constructor() {
    this.searchStore = new SearchStore(this);
  }
}
