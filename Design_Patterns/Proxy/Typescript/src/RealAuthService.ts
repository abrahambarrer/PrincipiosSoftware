export type {IAuthService} from "./IAuthService";
import * as data from "../data.json"
import { IAuthService } from "./IAuthService";

export class implements IAuthService {
    async login(correo: string, contrasenia: string): Promise<boolean> {
        if (data.email === correo && data.contra === contrasenia){
            return true;
        }
        return false;
    }

    async getProtectedData(): Promise<string> {
        return JSON.stringify();
    }
}