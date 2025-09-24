import {MedalProvider} from "../domain/MedalProvider";
import {MedalTable} from "../domain/MedalTable";

export class Paris2024Provider implements MedalProvider {
  top(n: number): MedalTable[] {
    const data : MedalTable[] = [
      {rank: 1, country: "usa", gold: 40, silver: 44, bronze: 42},
      {rank: 2, country: "chn", gold: 35, silver: 30, bronze: 35},
      {rank: 3, country: "jpn", gold: 27, silver: 20, bronze: 27},
      {rank: 4, country: "fra", gold: 17, silver: 26, bronze: 23},
      {rank: 5, country: "aus", gold: 22, silver: 21, bronze: 25}
    ];
    return data.slice(0, n);
  }
}