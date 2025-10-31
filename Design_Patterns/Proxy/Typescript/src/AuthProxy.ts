import { IAuthService } from "./IAuthService";

export class AuthProxy implements IAuthService {
    private realService : RealAuthService;
    isAuthenticated: boolean;

    constructor(realService: RealAuthService, initialLogStatus: boolean){
        this.realService = realService;
        this.isAuthenticated = initialLogStatus;
    }
    async login(correo: string, contrasenia: string) : Promise<boolean> {
        console.log("Interceptando intento de inicio de sesion");
        this.realService.login(correo, contrasenia);
    }

    async getProtectedData(): Promise<string> {
        if (this.isAuthenticated){
            return this,this.realService.getProtectedData();
        }
        return ""
    }
}