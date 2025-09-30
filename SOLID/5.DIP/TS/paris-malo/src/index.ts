class Paris2024Provider {
  top(n: number) {
    const data = [
      {rank: 1, country: "usa", gold: 40, silver: 44, bronze: 42},
      {rank: 2, country: "chn", gold: 35, silver: 30, bronze: 35},
      {rank: 3, country: "jpn", gold: 27, silver: 20, bronze: 27},
      {rank: 4, country: "fra", gold: 17, silver: 26, bronze: 23},
      {rank: 5, country: "aus", gold: 22, silver: 21, bronze: 25},
    ];
    
    return data.slice(0, n);
  }
}

class MedalService {
  private provider: Paris2024Provider;

  constructor(){
    this.provider = new Paris2024Provider();
  }

  showTop(n: number) : void {
    const rows = this.provider.top(n);

    console.log("\n=== Paris 2024 ===");
    console.table(rows);
  }
}

const medallero = new MedalService();
medallero.showTop(3);